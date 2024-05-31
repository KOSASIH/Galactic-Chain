pragma solidity ^0.6.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/SafeERC721.sol";

contract ERC721 {
    string public name;
    string public symbol;
    uint public totalSupply;
    mapping (address => uint) public balanceOf;
    mapping (uint => address) public ownerOf;
    mapping (uint => address) public approved;
    mapping (address => mapping (uint => bool)) public tokenOfOwner;

    event Transfer(address indexed from, address indexed to, uint indexed tokenId);
    event Approval(address indexed owner, address indexed approved, uint indexed tokenId);
    event ApprovalForAll(address indexed owner, address indexed operator, bool approved);

    constructor(string memory _name, string memory _symbol) public {
        name = _name;
        symbol = _symbol;
    }

    function mint(address _to, uint _tokenId) public {
        require(ownerOf[_tokenId] == address(0), "Token already exists");
        balanceOf[_to]++;
        ownerOf[_tokenId] = _to;
        tokenOfOwner[_to][_tokenId] = true;
        emit Transfer(address(0), _to, _tokenId);
    }

    function transfer(address _to, uint _tokenId) public {
        require(ownerOf[_tokenId] == msg.sender, "Only the owner can transfer");
        require(approved[_tokenId] == address(0) || approved[_tokenId] == _to, "Token is not approved for transfer");
        balanceOf[msg.sender]--;
        balanceOf[_to]++;
        ownerOf[_tokenId] = _to;
        tokenOfOwner[msg.sender][_tokenId] = false;
        tokenOfOwner[_to][_tokenId] = true;
        emit Transfer(msg.sender, _to, _tokenId);
    }

    function approve(address _approved, uint _tokenId) public {
        require(ownerOf[_tokenId] == msg.sender, "Only the owner can approve");
        approved[_tokenId] = _approved;
        emit Approval(msg.sender, _approved, _tokenId);
    }

    function setApprovalForAll(address _operator, bool _approved) public {
        emit ApprovalForAll(msg.sender, _operator, _approved);
    }
}
