## Penguins Project

### For EDA check:
```
Penguins
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

### For testing check:
```
Penguins
├── pyproject.toml
├── README.md
├── results
│   ├── adelie_bill_depth_boxplot.png
│   ├── adelie_bill_depth_histograms.png
│   └── adelie_bill_depth_qqplots.png
├── t_test_penguins.py 
└── uv.lock
```

## Clone the repository
`git clone https://github.com/kylezarif/penguins.git`
`cd penguins`

## Setup Instructions
###  Install `uv`
`uv` is a fast Python package and project manager.  
Run the following command in your terminal:

curl -LsSf https://astral.sh/uv/install.sh | sh

`export PATH="$HOME/.local/bin:$PATH"`

### Create and activate the environment using uv
`uv sync`
`source .venv/bin/activate`
