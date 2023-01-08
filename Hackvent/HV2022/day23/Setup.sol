// SPDX-License-Identifier: UNLICENSED

pragma solidity 0.8.16;

import "./Challenge.sol";

contract Setup {
    Challenge public challenge;

    constructor() {
        challenge = new Challenge(msg.sender);
    }

    function isSolved() public view returns (bool) {
        return challenge.solved();
    }
}
