// SPDX-License-Identifier: MIT

pragma solidity ^0.6.6;
// here a mild error used to come earlier so i removed it by changing the global compiler version from double click change it to 0.6.6

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";
// brownie can't understand these imports (i am not talking about verify and publish of etherscan but talking about that brownie can't understand and thus won't deploy these) 
// so we need to tell brownie import these from github instead of npm
// and luckily/intentionally there is a package out there to download chainlink contracts
// so we put dependency and we put remapping just these 2 things
// so remapped to some address present over github

// now after this when we compile it for the first time we see that in dependencies section it has downloaded above imports

contract FundMe2 {
    using SafeMathChainlink for uint256;

    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;
    AggregatorV3Interface public priceFeed;    // change 2


    constructor(address _priceFeed) public {  // change 1
        priceFeed= AggregatorV3Interface(_priceFeed);  //change 3
        owner = msg.sender;
    }

    function fund() public payable {
        uint256 mimimumUSD = 50 * 10**18;
        require(
            getConversionRate(msg.value) >= mimimumUSD,
            "You need to spend more ETH!"
        );
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }

    // 1000000000
    function getConversionRate(uint256 ethAmount)
        public
        view
        returns (uint256)
    {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }

    function getEntranceFee() public view returns(uint256) {
        uint256 mimimumUSD= 50 * 10**18;
        uint256 price= getPrice();
        uint256 precision= 1* 10**18;
        return (mimimumUSD * precision) /price;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function withdraw() public payable onlyOwner {
        msg.sender.transfer(address(this).balance);

        for (
            uint256 funderIndex = 0;
            funderIndex < funders.length;
            funderIndex++
        ) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }
}
