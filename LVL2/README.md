## Second problem description

Given a list of elevator versions represented as string, write a function solution(l) that returns the same list sorted in ascending order by major, minor and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision number, then it will also have a minor number. 

For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.12", "1.0.2"], the function solution(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0","1.0.0"]. The number of elements of elements in the list l will be at least 1 and will not exceed 100.


input: ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

output: 0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0

input: ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.12", "1.0.2"]

output: 1.0,1.0.2,1.0.12,1.1.2,1.3.3