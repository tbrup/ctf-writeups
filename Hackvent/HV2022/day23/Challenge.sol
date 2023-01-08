// SPDX-License-Identifier: UNLICENSED

pragma solidity 0.8.16;

contract Challenge {
    bool public solved = false;
    address public signer;

    constructor(address _signer) {
        signer = _signer;
    }

    function solve(
        address helper,
        bytes memory sig,
        bytes calldata message
    ) external {
        for (uint256 i = 0; i < 19; i++) {
            require(bytes20(helper)[i] == 0, "helper has not enought 0s");
        }

        bytes32 r;
        bytes32 s;
        uint8 v = 28;
        assembly {
            // first 32 bytes, after the length prefix
            r := mload(add(sig, 32))
            // second 32 bytes
            s := mload(add(sig, 64))
        }

        (bool success, bytes memory result) = helper.call(
            abi.encode(keccak256(message), v, r, s)
        );
        require(success, "helper call failed");
        require(bytes32(result) == bytes32(uint256(uint160(signer))), "Wrong Signer!");
        solved = true;
    }
}
