from templates import make_suite as _make_suite

_benchmarks = [
    {
     'obj': 'LinearRegression',
     'init_params': {},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'Ridge',
     'init_params': {'alpha': 0.1, 'normalize': False},
     'datasets': ('minimadelon', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'Lars',
     'init_params': {'normalize': False},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'LassoLars',
     'init_params': {'alpha': 0.1, 'normalize': False},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'Lasso',
     'init_params': {'alpha': 0.1, 'normalize': False},
     'datasets': ('arcene', 'madelon'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'ElasticNet',
     'init_params': {'rho': 0.5, 'alpha': 0.5},  # normalize here?
     'datasets': ('arcene', 'blobs'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'OrthogonalMatchingPursuit',
     'init_params': {'n_nonzero_coefs': 10},
     'datasets': ('minimadelon', 'blobs'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'SGDClassifier',
     'init_params': {},
     'datasets': ('madelon', 'newsgroups'),
     'statements': ('fit', 'predict')
    },
    {
     'obj': 'LogisticRegression',
     'init_params': {'C': 1e5},
     'datasets': ('minimadelon-oney', 'blobs'),
     'statements': ('fit', 'predict')
    }
]

suite = _make_suite(config_arg_list=_benchmarks)
