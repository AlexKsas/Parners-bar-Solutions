import axios from "axios";
import { useState } from "react";
import { View, Text, TextInput, StyleSheet, Alert, TouchableOpacity, ScrollView } from "react-native"

const Datos = () => {

  const [nombre, setNombre] = useState('')
  const [email, setEmail] = useState('')
  const [telefono, setTelefono] = useState('')
  const [tipoDocumento, setTipoDocumento] = useState('')
  const [documento, setDocumento] = useState('')

  const handleSubmit = async () => {
    let url = 'http://localhost:8000/registro/'
    const res = await axios.post(url,{
      "usuario":"usuario",
      "contrasena":"123456789"
    })
    console.log("res ", res)
    Alert.alert(`${nombre}, ${email}, ${telefono}, ${tipoDocumento}, ${documento}`)
  }

  return (
    <View style={styles.form}>
      <ScrollView>
      <Text style={styles.label}>Nombre:</Text>
      <TextInput style={styles.input}
        placeholder="ingresar nombre"
        value={nombre}
        onChangeText={setNombre} />

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

      <Text style={styles.label}>Tipo de Documento:</Text>
      <TextInput style={styles.input}
        placeholder="Seleccionar una opcion"
        value={tipoDocumento}
        onChangeText={setTipoDocumento} />

      <Text style={styles.label}>Numero de Documento:</Text>
      <TextInput style={styles.input}
        placeholder="ingresar Numero de documento"
        value={documento}
        onChangeText={setDocumento} />

      <TouchableOpacity onPress={handleSubmit} style={styles.submit}>
        <Text style={styles.submitText}>➡️</Text>
      </TouchableOpacity>
    </ScrollView>
    </View>
  )
}

const styles = StyleSheet.create({
  input: {
    height: 40,
    margin: 25,
    marginTop: 0,
    borderWidth: 0.5,
    padding: 10,
    borderRadius: 10,
    borderColor: '#FFFFFF'
  },
  form: {
    flex: 1,
    backgroundColor: '#92B4EC',
    padding: 16,
    justifyContent: "center",
    alignItems: 'center',
  },
  label: {
    fontSize: 20,
    marginLeft:25,
    color: '#FFFFFF'
  },
  submit: {
    backgroundColor: 'white',
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 15,
    marginLeft: 285
  },
  submitText: {
    fontSize: 20,
    alignItems: 'center',
  }
});

export default Datos;