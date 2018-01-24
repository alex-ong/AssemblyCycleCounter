from InstructionTable import InstructionTable
import io

INSTRUCTION_SET = "ATMega32u4"

targetFile = "non-bitshifter.txt"
outputFile = "non-bitshifter-annotated.txt"

total_cost_min = 0

def ignoreline(line):
    return len(line) < 5 or line[4] == ':'
    
def getInstruction(line):
    try:
        offset = len(" 170 005a C501      		");
        instruction = line[offset:offset+5]        
        instruction = instruction.strip()
        if (" " in instruction):
            instruction = instruction.split(" ")[0]
        instruction = instruction.upper()        
    except:
        return None
    return instruction
    
def processLine(line, it):
    global total_cost_min
    instruction = getInstruction(line)
    if instruction is not None:
        cost = it.map(instruction.upper())
        if cost is not None:
            if "/" in cost:
                costs = cost.split("/")
                total_cost_min += int(costs[0])
            else:
                total_cost_min += int(cost)
            return "(cost:" + cost + ")" + line

    return line 
        
if __name__ == '__main__':
    it = InstructionTable(INSTRUCTION_SET)
    outputLines = []
    with (open(targetFile)) as f:
        for line in f:
            if (ignoreline(line)):
                outputLines.append(line)
            else:
                outputLines.append(processLine(line, it))
    
    with (open(outputFile, 'w')) as f:
        f.writelines(outputLines)
        f.write("\ntotal cost (choosing min)" + str(total_cost_min) + "\n")