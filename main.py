from fp_wrapper import solve_system


def run_case(x1_0,x2_0,tol,max_iter,scale):
  x1,x2,iter = solve_system((x1_0,x2_0,tol=tol,max_iter=max_iter,scale=scale)


def unit_test():
  run_case(0.5, 0.5, tol = 1e-6, max_iteration = 1000, scale = 0.1)
  run_case(1.5, 0.8, tol = 1e-8, max_iteration = 1000, scale = 1.0)
  run_case(0.2, 1.0, tol = 1e-9, max_iteration = 1000, scale = 0.5)
  run_case(0.3, 2.0, tol = 1e-4, max_iteration = 1000, scale = 0.6)
  run_case(2.0, 2.5, tol = 1e-3, max_iteration = 1000, scale = 0.12)
  run_case(0.7, 0.2, tol = 1e-9, max_iteration = 1000, scale = 0.7)


if __name__ == "__main__":
  unittest()

  
