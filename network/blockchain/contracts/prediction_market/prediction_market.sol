pragma solidity ^0.8.0;

contract PredictionMarket {
    mapping (address => uint) public bets;
    mapping (address => uint) public outcomes;
    uint public totalBets;
    uint public outcomeCount;

    function bet(uint _outcome) public payable {
        require(msg.sender!= address(0), "Invalid sender");
        require(_outcome >= 0 && _outcome < outcomeCount, "Invalid outcome");
        bets[msg.sender] = _outcome;
        totalBets += msg.value;
    }

    function resolve(uint _outcome) public {
        require(msg.sender!= address(0), "Invalid sender");
        require(_outcome >= 0 && _outcome < outcomeCount, "Invalid outcome");
        for (address bettor in bets) {
            if (bets[bettor] == _outcome) {
                // reward the bettor
                // e.g. transfer funds, update state, etc.
            }
        }
    }
}
