// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentInfo {
    struct Student {
        uint256 id;
        string name;
        uint256 marks;
    }

    Student[] public students;

    event FallbackCalled(address sender, uint256 value);

    function addStudent(uint256 _id, string memory _name, uint256 _marks) public {
        students.push(Student(_id, _name, _marks));
    }

    function getStudent(uint256 index) public view returns (uint256, string memory, uint256) {
        Student memory s = students[index];
        return (s.id, s.name, s.marks);
    }

    function getCount() public view returns (uint256) {
        return students.length;
    }

    fallback() external payable {
        emit FallbackCalled(msg.sender, msg.value);
    }
}
