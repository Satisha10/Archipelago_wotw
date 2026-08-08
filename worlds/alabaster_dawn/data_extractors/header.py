"""Function to generate the header that appears as a docstring on top of the generated files."""

def header_py(file_name: str, function_name: str | None = None) -> str:
    """
    Generate the header for AP World files (python).

    :param file_name: File name where the generated data is created.
    :param function_name: Function that generates the data (optional).
    """
    output = (
        '"""Generated data, DO NOT MODIFY HERE.\n'
        'Check the `data_extractors` folder to see how to generate this file or to make modifications.\n'
    )
    output += f"This file got generated in `{file_name}`"
    if function_name is not None:
        output += f' with `{function_name}`."""\n\n'
    else:
        output += f'."""\n\n'

    return output


def header_ts(file_name: str, function_name: str | None = None) -> str:
    """
    Generate the header for client files (typescript files).

    :param file_name: File name where the generated data is created.
    :param function_name: Function that generates the data (optional).
    """
    output = '''// Generated data, DO NOT MODIFY HERE.
// Check the `data_extractors` folder in the AP World source code at
// https://github.com/Satisha10/Archipelago_wotw/tree/alabaster-dawn/worlds/alabaster_dawn/data_extractors
// to see how to generate this file or to make modifications.
'''
    output += f"// This file got generated in `{file_name}`"
    if function_name is not None:
        output += f' with `{function_name}`."""\n\n'
    else:
        output += f'."""\n\n'

    return output
