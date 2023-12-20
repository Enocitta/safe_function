import inspect
import logging

logger = logging.getLogger(__name__)


def __check_main_loop(a, dtipe, numTypes, counter):
    if (type(a) is not dtipe.annotation) and (dtipe.annotation != dtipe.empty) and numTypes == 0:
        logger.warning('variable de tipo incorrecta: "{}", es de Tipo {} cuando el parametro soportado es '
                       'de tipo {} '.format(a, type(a), dtipe.annotation))
        counter = counter + 1
    elif numTypes >= 1:
        if type(a) not in dtipe.annotation:
            # print('variable de tipo incorrecta: "{}", es de Tipo {} cuando el parametro soportado es '
            #    'de tipo {} '.format(a, type(a), dtipe.annotation))
            logger.warning('variable de tipo incorrecta: "{}", es de Tipo {} cuando el parametro soportado es '
                           'de tipo {} '.format(a, type(a), dtipe.annotation))

            counter = counter + 1
    else:
        # print("pass")
        logger.info("safe parameter OK")
    return counter


def safe_function(function):
    def wrapper(*args):
        counter = 0
        paramTipe = {"POSITIONAL_ONLY": 0, "POSITIONAL_OR_KEYWORD": 0, "VAR_POSITIONAL": 0, "KEYWORD_ONLY": 0,
                     "VAR_KEYWORD": 0, }
        arguments = []
        defaultParam = 0
        if inspect.isfunction(function):

            param_function = inspect.signature(function).parameters
            for dido in param_function.values():  # Count types of parameters to determine minimum necessary parameters.
                arguments.append(
                    {"name": dido.name, "default": dido.default, "annotation": dido.annotation, "empty": dido.empty,
                     "kind": dido.kind, })
                if dido.kind == dido.POSITIONAL_ONLY:
                    paramTipe["POSITIONAL_ONLY"] += 1
                elif dido.kind == dido.POSITIONAL_OR_KEYWORD:
                    paramTipe["POSITIONAL_OR_KEYWORD"] += 1
                elif dido.kind == dido.VAR_POSITIONAL:
                    paramTipe["VAR_POSITIONAL"] += 1
                elif dido.kind == dido.KEYWORD_ONLY:
                    paramTipe["KEYWORD_ONLY"] += 1
                elif dido.kind == dido.VAR_KEYWORD:
                    paramTipe["VAR_KEYWORD"] += 1

                if dido.default is not dido.empty:
                    defaultParam += 1

            if ((len(arguments) - (paramTipe["VAR_POSITIONAL"] + paramTipe["KEYWORD_ONLY"] +
                                   paramTipe["VAR_KEYWORD"] + defaultParam)) <= args.__len__()):

                posvar = 0

                for a, dtipe in zip(args, param_function.values()):

                    numTypes = 0
                    annType = dtipe.annotation
                    numTypes = len(tuple(annType)) if type(annType) is not type else numTypes

                    if (dtipe.kind == dtipe.POSITIONAL_OR_KEYWORD) or (dtipe.kind == dtipe.POSITIONAL_ONLY):

                        counter = __check_main_loop(a, dtipe, numTypes, counter)

                    elif dtipe.kind == dtipe.VAR_POSITIONAL:
                        if type(args) is tuple:
                            for vars in args[posvar:]:
                                counter = __check_main_loop(vars, dtipe, numTypes, counter)

                        else:
                            counter = __check_main_loop(a, dtipe, numTypes, counter)

                    posvar += 1
                if counter == 0:
                    return function(*args)
                else:
                    # print("La Funcion '{}' no se ejecutara por ser llamada con parametros no soportados".format(
                    #    function.__name__))
                    logger.warning(
                        "La Funcion '{}' no se ejecutara por ser llamada con parametros no soportados".format(
                            function.__name__))
                    return

            else:  # esta algo mal con la invocacion y sus parametros
                # print(  "hay algo mal en la invocacion de '{}'".format(function.__str__()) )
                logger.error("Faltan arguments obligatorios en la invocacion de '{}'".format(function.__name__))
                return

        else:
            raise TypeError("SOLO USAR UNA FUNCION CON ESTE DECORADOR")

    return wrapper
