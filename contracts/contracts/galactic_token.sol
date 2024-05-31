pragma solidity ^0.6.0;

import "./erc20.sol";
import "./erc721.sol";

contract GalacticToken is ERC20, ERC721 {
    string public name;
    string public symbol;
    uint public totalSupply;

    constructor(string memory _name, string memory _symbol, uint _totalSupply) public {
        name = _name;
        symbol = _symbol;
        totalSupply = _totalSupply;
    }

    function mint(address _to, uint _amount) public {
        require(totalSupply + _amount <= totalSupply, "Total supply exceeded");
        totalSupply += _amount;
        balanceOf[_to] += _amount;
        emit Transfer(address(0), _to, _amount);
    }

    function mint(address _to, uint _tokenId) public {
        require(ownerOf[_tokenId] == address(0), "Token already exists");
        balanceOf[_to]++;
        ownerOf[_tokenId] = _to;
        tokenOfOwner[_to][_tokenId] = true;
        emit Transfer(address(0), _to, _tokenId);
    }
}
