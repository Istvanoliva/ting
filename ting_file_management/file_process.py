from ting_file_management.file_management import txt_importer
import sys


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
    if not instance.__len__():
        print("Não há elementos")
        return

    removed = instance.dequeue()

    print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write('Posição inválida\n')
