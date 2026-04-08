class Counter:
    def __init__(self, mode="side", line_pos=320):
        self.mode = mode
        self.line = line_pos
        self.entry = 0
        self.exit = 0
        self.memory = {}

    def update(self, obj_id, cx, cy, bottom):
        if obj_id not in self.memory:
            self.memory[obj_id] = {
                "last_x": cx,
                "last_y": bottom,
                "counted": False
            }

        prev_x = self.memory[obj_id]["last_x"]
        prev_y = self.memory[obj_id]["last_y"]

        if not self.memory[obj_id]["counted"]:

            if self.mode == "side":
                if prev_x < self.line and cx >= self.line:
                    self.entry += 1
                    self.memory[obj_id]["counted"] = True
                elif prev_x > self.line and cx <= self.line:
                    self.exit += 1
                    self.memory[obj_id]["counted"] = True

            else:  # top
                if prev_y < self.line and bottom >= self.line:
                    self.entry += 1
                    self.memory[obj_id]["counted"] = True
                elif prev_y > self.line and bottom <= self.line:
                    self.exit += 1
                    self.memory[obj_id]["counted"] = True

        self.memory[obj_id]["last_x"] = cx
        self.memory[obj_id]["last_y"] = bottom