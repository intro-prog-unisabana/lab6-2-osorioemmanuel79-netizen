# Write your code here!
def employee_print(employee_info):
    # Imprimir datos base
    name = employee_info.get("Name", "N/A")
    salary = employee_info.get("Salary", "N/A")
    role = employee_info.get("Role", "N/A")

    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")

    # Crear una copia para no modificar el diccionario original
    extra_info = employee_info.copy()

    # Eliminar claves base si existen
    extra_info.pop("Name", None)
    extra_info.pop("Salary", None)
    extra_info.pop("Role", None)

    # Imprimir información adicional
    if extra_info:
        for key, value in extra_info.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")