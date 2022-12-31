def exists_word(word, instance):
    occurrencies = list()

    for item in range(len(instance)):
        row = instance.search(item)

        list_data = [
                {"linha": (index + 1)}
                for index, line in enumerate(row['linhas_do_arquivo'])
                if word.lower() in line.lower()
            ]

        file_dict = {
                "palavra": word,
                "arquivo": row["nome_do_arquivo"],
                "ocorrencias": list_data,
        }

        if not len(file_dict["ocorrencias"]):
            return []

        if file_dict:
            occurrencies.append(file_dict)

        return occurrencies


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
