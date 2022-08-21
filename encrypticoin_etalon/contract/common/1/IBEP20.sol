// SPDX-License-Identifier: Apache-2.0

pragma solidity ^0.8.0;

import "../../openzeppelin-contracts/4.5.0/token/ERC20/extensions/IERC20Metadata.sol";

interface IBEP20 is IERC20Metadata {

    /**
     * @dev Returns the bep token owner.
     */
    function getOwner() external view returns (address);

}