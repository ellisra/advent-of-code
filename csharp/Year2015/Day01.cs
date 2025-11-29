namespace csharp.Year2015;

public class Day01 : ISolution {
    public void Solve() {
        List<char> input = [.. File.ReadAllText("../inputs/2015/day01.txt").Trim()];

        Console.WriteLine($"Part 1: {input.Count - 2 * input.Count(item => item == ')')}");
        Console.WriteLine($"Part 2: {GetNegativeStep(input)}");
    }

    private static int GetNegativeStep(List<char> input) {
        int floorNum = 0;
        for (int i = 0; i < input.Count; i++) {
            if (floorNum < 0) {
                return i;
            }

            if (input[i] == '(') {
                floorNum++;
            } else {
                floorNum--;
            }
        }

        return 0;
    }
}
