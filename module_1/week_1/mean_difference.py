def mean_diff_of_n_th_root_error(y, y_hat, n, p):
    y_root = pow(y, (1/n))
    y_hat_root = pow(y_hat, (1/n))
    md_of_re = y_root - y_hat_root
    loss = pow(md_of_re, p)
    print(loss)


mean_diff_of_n_th_root_error(y=100, y_hat=99.5, n=2, p=1)
mean_diff_of_n_th_root_error(y=50, y_hat=49.5, n=2, p=1)
mean_diff_of_n_th_root_error(y=20, y_hat=19.5, n=2, p=1)
mean_diff_of_n_th_root_error(y=0.6, y_hat=0.1, n=2, p=1)
