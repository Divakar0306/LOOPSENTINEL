with open("loopsentinel/analyzer.py") as f:
    code = f.read()

# Enhance _static_analyze to harvest initial assignments before the while loop
old_fn = """    def _static_analyze(self, tree: ast.AST, env: Dict[str, int]) -> Dict[str, Any]:
        loops = [n for n in ast.walk(tree) if isinstance(n, ast.While)]
        if not loops:
            return {"verdict": "HALTS", "proof": "Program contains no loop constructs (straight-line CFG)."}"""

new_fn = """    def _static_analyze(self, tree: ast.AST, env: Dict[str, int]) -> Dict[str, Any]:
        # Harvest constant assignments from top-level before while loops
        env = dict(env)
        for node in getattr(tree, 'body', []):
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                if isinstance(node.value, ast.Constant) and isinstance(node.value.value, int):
                    env[node.targets[0].id] = node.value.value
            elif isinstance(node, ast.While):
                break

        loops = [n for n in ast.walk(tree) if isinstance(n, ast.While)]
        if not loops:
            return {"verdict": "HALTS", "proof": "Program contains no loop constructs (straight-line CFG)."}"""

code = code.replace(old_fn, new_fn)
with open("loopsentinel/analyzer.py", "w") as f:
    f.write(code)
print("Updated analyzer static analysis environment extraction.")
