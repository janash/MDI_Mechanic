"""
mdi_mechanic.py
A tool for testing and developing MDI-enabled projects.

Handles the primary functions
"""

####
import os
import traceback
from . import report
from . import install

def get_calling_path():
    # Get the name of the file that called the calling function
    caller_name = traceback.extract_stack()[-3][0]

    # Get the path to the file that called this function
    caller_path = os.path.realpath( caller_name )
    caller_directory = os.path.dirname( caller_path )
    
    return caller_directory
    


def command_report():
    print("Starting a report")
    report_dir = os.getcwd()
    report.generate_report( report_dir )



def command_build():
    print("Starting the installation")
    report_dir = os.getcwd()
    install.install_all( report_dir )



def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
