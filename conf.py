# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'readthedoc_john'
copyright = '2026, John'
author = 'John'
release = '2026/03/12'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# --- 擴充功能設定 ---
extensions = [
    'myst_parser',  # 取代舊有的 recommonmark 相關設定
]
# --- 支援的文件副檔名 ---
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# --- MyST Parser 進階設定 ---
myst_enable_extensions = [
    "colon_fence",    # 支援 ::: 語法製作警告框
    "deflist",       # 支援定義列表
    "tasklist",      # 支援 - [ ] 任務列表
    "fieldlist",     # 支援文件元數據欄位
]

# Ensure the static path is set
html_static_path = ['_static']

# Add the custom CSS file
def setup(app):
    app.add_css_file('custom.css')

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'  # 這裡要改成 rtd 主題

html_static_path = ['_static']
