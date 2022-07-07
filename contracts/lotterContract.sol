// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

contract Lottery{
    
 address public manager;

 address[] public players;
 

   constructor() {
    manager = msg.sender;}
 
  function enter() public payable {
    
    // we can pass some code in it and if it return ture then function will continue and if it return false then the function will terminate over here


// this will check weather the amount of eather sent by the player is > .01 or not and if it become false then the function will termiante over here only 

    require(msg.value > .01 ether);
    players.push(msg.sender);}

}