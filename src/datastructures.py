
"""
actualice este archivo para implementar los siguientes métodos ya declarados:
- add_member: debe agregar un miembro a la lista self._members
- eliminar_miembro: debe eliminar un miembro de la lista self._members
- update_member: debe actualizar un miembro de la lista self._members
- get_member: debe devolver un miembro de la lista self._members

"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
         # El apellido de la familia se asigna al objeto
        self.last_name = last_name

        # example list of members
        self._members = [
            {'id': self._generateId(), 
             'first name': 'John', 
             'last name': self.last_name,
             'age': '33', 
             'lucky numbers': [7, 13, 22],
             },
             {'id': self._generateId(), 
             'first name': 'Jane', 
             'last name': self.last_name,
             'age': '35', 
             'lucky numbers': [10, 14, 3]},
             {'id': self._generateId(), 
             'first name': 'Jimmy', 
             'last name': self.last_name,
             'age': '5', 
             'lucky numbers': [1]}
             ]

    #  use este método para generar ID de miembros aleatorios al agregar miembros a la lista
    def _generateId(self):
        return randint(0, 99999999)
    
    
    # Método para agregar un nuevo miembro a la familia
    def add_member(self, member):
        # Si el miembro no tiene un ID, se genera uno automáticamente
        if not member['id']:
            member['id']=self._generateId()
        # Añadir el miembro a la lista de miembros
        self._members.append(member)
        # Devolver el miembro agregado
        return member
    
 
     # Método para eliminar un miembro de la familia por su ID
    def delete_member(self, id):       
        for member in self._members:  # Itera sobre la lista de miembros
            if member['id']==id: # Si se encuentra el miembro con el ID dado
                self._members.remove(member) # Eliminar el miembro de la lista
                return {'done': True} # Devolver un mensaje indicando que se eliminó correctamente
        return {'done': False} # Si no se encontró el miembro, devolver un mensaje de error
    

    # Método para obtener un miembro específico por su ID
    def get_member(self, id): 
       for member in self._members: # Itera sobre la lista de miembros
            if member['id']==id:  # Si se encuentra el miembro con el ID dado
                return member # Devolver el miembro encontrado

    # este método está hecho, devuelve una lista con todos los miembros de la familia
    def get_all_members(self):
        return self._members
