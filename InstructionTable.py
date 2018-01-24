class InstructionTable(object):
    def __init__(self, target):
        self.instructions = {}
        with open(target + ".txt") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                instruction, cost = line.split()
                self.instructions[instruction] = cost
    
    def map(self, instruction):
        result = None
        if instruction in self.instructions:
            result = self.instructions[instruction]
        return result
        