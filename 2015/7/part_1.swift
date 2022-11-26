import Foundation

guard
    let input = try? String(
        contentsOfFile: "input.txt")
else {
    print("failed to read file")
    throw NSError(domain: "", code: 0)
}

var availableLines = input.split(separator: "\n")

var wiresDict = [String: UInt16]()

while availableLines.count > 0 {
    // remove if the line was already processed
    if let i = availableLines.firstIndex(of: "-1") {
        availableLines.remove(at: i)
        continue
    }

    for (i, line) in availableLines.enumerated() {
        let elements = line.split(separator: " ")

        if elements.count == 3 {
            // "straight wiring"
            if let numberValue = UInt16(elements[0]) {
                wiresDict[String(elements[elements.count - 1])] = numberValue
            } else {
                if let wireValue = wiresDict[String(elements[0])] {
                    wiresDict[String(elements[elements.count - 1])] = wireValue
                } else {
                    continue
                }
            }
        } else if elements.count == 4 {
            // "not"
            if let secondElement = UInt16(elements[1]) {
                wiresDict[String(elements[elements.count - 1])] = ~secondElement
            } else if let secondElement = wiresDict[String(elements[1])] {
                wiresDict[String(elements[elements.count - 1])] = ~secondElement
            } else {
                continue
            }
        } else if elements.count == 5 {
            // "binaryOp"
            var firstElement: UInt16 = 0
            var secondElement: UInt16 = 0

            if let numberValue = UInt16(elements[0]) {
                firstElement = numberValue
            } else if let numberValue = wiresDict[String(elements[0])] {
                firstElement = numberValue
            } else {
                continue
            }

            if let numberValue = UInt16(elements[2]) {
                secondElement = numberValue
            } else if let numberValue = wiresDict[String(elements[2])] {
                secondElement = numberValue
            } else {
                continue
            }

            let bitwiseOp = String(elements[1])
            if bitwiseOp == "AND" {
                wiresDict[String(elements[elements.count - 1])] = firstElement & secondElement
            } else if bitwiseOp == "OR" {
                wiresDict[String(elements[elements.count - 1])] = firstElement ^ secondElement
            } else if bitwiseOp == "LSHIFT" {
                wiresDict[String(elements[elements.count - 1])] = firstElement << secondElement
            } else if bitwiseOp == "RSHIFT" {
                wiresDict[String(elements[elements.count - 1])] = firstElement >> secondElement
            }

        }
        // flag the line as "processed"
        availableLines[i] = "-1"
    }
}

if let a = wiresDict["a"] {
    print(a)
}
