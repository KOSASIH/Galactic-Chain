pragma solidity ^0.8.0;

contract DAO {
    address[] public members;
    mapping (address => uint) public votes;
    uint public quorum;
    uint public proposalCount;

    constructor(address[] memory _members, uint _quorum) public {
        members = _members;
        quorum = _quorum;
    }

    function propose(address[] memory _targets, uint[] memory _values) public {
        require(msg.sender!= address(0), "Invalid sender");
        require(members[msg.sender]!= 0, "Not a member");
        proposalCount++;
        for (uint i = 0; i < _targets.length; i++) {
            votes[_targets[i]] = _values[i];
        }
    }

    function vote(address _target) public {
        require(msg.sender!= address(0), "Invalid sender");
        require(members[msg.sender]!= 0, "Not a member");
        votes[_target]++;
        if (votes[_target] >= quorum) {
            executeProposal(_target);
        }
    }

    function executeProposal(address _target) internal {
        // execute the proposal logic here
        // e.g. transfer funds, update state, etc.
    }
}
