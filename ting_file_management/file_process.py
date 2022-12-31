from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if (path_file) in str(instance._data):
        return

    lists = txt_importer(path_file)

    files = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lists),
        "linhas_do_arquivo": lists,
    }

    instance.enqueue(files)
    print(files)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
