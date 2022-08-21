// SPDX-License-Identifier: Apache-2.0

pragma solidity 0.8.13;

import "./openzeppelin-contracts/4.5.0/token/ERC20/ERC20.sol";
import "./openzeppelin-contracts/4.5.0/access/Ownable.sol";
import "./common/1/IBEP20.sol";

contract BEP20EtalonToken is ERC20, Ownable, IBEP20 {
    constructor() ERC20("Etalon", "ETA") {
        _mint(msg.sender, 5000000 * 10 ** decimals());
    }

    /**
     * @dev Returns the bep token owner.
     */
    function getOwner() external view returns (address) {
        return owner();
    }
}
