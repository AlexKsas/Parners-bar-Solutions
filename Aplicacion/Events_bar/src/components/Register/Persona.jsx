import { useState } from "react";
import { View, Text, TextInput, StyleSheet, Alert, TouchableOpacity, ScrollView, Image } from "react-native";
// import RNPickerSelect from 'react-native-picker-select'

const Persona = () => {

  const [nombre, setNombre] = useState('')
  const [email, setEmail] = useState('')
  const [telefono, setTelefono] = useState('')
  const [tipoDocumento, setTipoDocumento] = useState(null)
  const [documento, setDocumento] = useState('')

  const handleSubmit = () => {
    Alert.alert('Usuario registrado correctamente')
  }
  const options = [
    { label: 'Opción 1', value: 'opcion1' },
    { label: 'Opción 2', value: 'opcion2' },
    { label: 'Opción 3', value: 'opcion3' },
  ]

  const placeholder = {
    label: 'Selecciona una opción...',
    value: null,
  };


  return (
    <View style={styles.form}>
      <ScrollView>
        <View>
          <Text style={[styles.label, { marginTop: 50 }]}>Nombre:</Text>
          {/* <Image source={require('../../Iconos/usuario.png')} style={styles.icon} /> */}
          <TextInput style={styles.input}
            placeholder="ingresar nombre"
            value={nombre}
            onChangeText={setNombre} />
        </View>

        <Text style={styles.label}>Apellidos:</Text>
        <TextInput style={styles.input}
          placeholder="ingresar Email"
          value={email}
          onChangeText={setEmail} />

        <Text style={styles.label}>Email:</Text>
        <TextInput style={styles.input}
          placeholder="ingresar Email"
          value={email}
          onChangeText={setEmail} />

        <Text style={styles.label}>Telefono:</Text>
        <TextInput style={styles.input}
          placeholder="ingresar Telefono"
          value={telefono}
          onChangeText={setTelefono} />
        {/* <View>
        <Text style={styles.label}>Tipo de Documento:</Text>
        <RNPickerSelect
          placeholder={placeholder}
          onValueChange={(value) => setTipoDocumento(value)}
          items={options}
          value={tipoDocumento}
        />
        </View> */}

        <Text style={styles.label}>Numero de Documento:</Text>
        <TextInput style={styles.input}
          placeholder="ingresar Numero de documento"
          value={documento}
          onChangeText={setDocumento} />

        <TouchableOpacity onPress={handleSubmit} style={styles.submit}>
          <Text style={styles.submitText}>Continuar</Text>
        </TouchableOpacity>
      </ScrollView>
    </View>
  )
}

const styles = StyleSheet.create({
  input: {
    height: 40,
    borderColor: '#4D4C7D',
    backgroundColor: '#F5F5F5',
    marginRight: 'auto',
    marginLeft: "auto",
    width: 280,
    borderRadius: 15
  },
  icon: {
    backgroundColor: "red",
    borderRadius: 25,
    height: 40,
    width: 40
  },
  form: {
    flex: 1,
    backgroundColor: '#363062',
    height: '100%'
  },
  label: {
    fontSize: 20,
    color: '#F5F5F5',
    marginRight: "auto",
    marginLeft: "auto",
    marginBottom: 5,
    marginTop: 25
  },
  submit: {
    backgroundColor: '#F99417',
    marginRight: "auto",
    marginLeft: "auto",
    borderRadius: 15,
    marginTop: 40
  },
  submitText: {
    fontSize: 24,
    alignItems: 'center',
    padding: 10
  }
});

export default Persona
