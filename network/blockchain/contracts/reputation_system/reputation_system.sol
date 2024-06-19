pragma solidity ^0.8.0;

contract ReputationSystem {
    mapping (address => uint) public reputation;
    mapping (address => mapping (address => uint)) public ratings;

    function rate(address _target, uint _rating) public {
        require(msg.sender!= address(0), "Invalid sender");
        require(_rating >= 0 && _rating <= 5, "Invalid rating");
        ratings[msg.sender][_target] = _rating;
        updateReputation(_target);
    }

    function updateReputation(address _target) internal {
        uint totalRating = 0;
        uint count = 0;
        for (address rater in ratings) {
            totalRating += ratings[rater][_target];
            count++;
        }
        reputation[_target] = totalRating / count;
    }

    function getReputation(address _target) public view returns (uint) {
        return reputation[_target];
    }
}
