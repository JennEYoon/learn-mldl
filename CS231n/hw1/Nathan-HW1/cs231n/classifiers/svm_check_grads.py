
def err(x,y):
  grad_numerical  = x
  grad_analytic   = y
  rel_error = (abs(grad_numerical - grad_analytic) /
              (abs(grad_numerical) + abs(grad_analytic)))
  print(rel_error)
  return rel_error


if __name__=="__main__":
  err(9,9)
  err(1,999)
