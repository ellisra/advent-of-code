using System.Reflection;
using csharp;

if (args.Length < 2) {
    Console.WriteLine("Usage: dotnet run <year> <day>");
    return;
}

var year = args[0];
var day = int.Parse(args[1]);

var typeName = $"csharp.Year{year}.Day{day:D2}";
var type = Assembly.GetExecutingAssembly().GetType(typeName);

if (type == null) {
    Console.WriteLine($"Year {year}, Day {day} is not yet implemented");
    return;
}

var solution = Activator.CreateInstance(type) as ISolution;
solution?.Solve();
