import React from 'react'
import { View, Image, StyleSheet, Text } from 'react-native'

const Inicio = () => {
    return (
        <View style={styles.container}>
            <Text style={styles.title}>Selecciona un tipo</Text>
            <Text style={[styles.title, {marginBottom: 30}]}>de registro</Text>
        {/* //     <View style={styles.container_img}> */}
            <Text style={styles.label}>Usuario</Text>
                <Image style={[styles.img, {marginBottom: 30}]} source={require('../../imagenes/amigos.png')} />
            <Text style={styles.label}>Establecimiento</Text>
                <Image style={styles.img} source={require('../../imagenes/bar.png')} />
            {/* // </View> */}
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        // padding: 30,
        // marginTop: "7%",
        backgroundColor: "#363062",
        height: '100%'
    },
    img: {
        width: 150,
        height: 150,
        borderRadius:50,
        backgroundColor: "#F99417",
        marginRight: 'auto',
        marginLeft: 'auto',
        marginBottom: 80 
    },
    title: {
        fontSize: 50,
        fontWeight: 'bold',
        marginLeft: 'auto',
        marginRight: 'auto',
        color: '#F5F5F5',
        marginTop: 20
    },
    label: {
        marginRight: 'auto',
        marginLeft: 'auto',
        marginTop: 31,
        fontSize: 30,
        color: '#F5F5F5'
    }
})

export default Inicio