import { Image, ScrollView, Text, View, StyleSheet } from "react-native"

const Productos = () => {

    const bebidas = [
        {
            "id": "1",
            "Nombre": "Cerveza",
            "Imagen": "https://img.freepik.com/vector-gratis/cervezas-ricas-frescas_603843-1287.jpg"
        },
        {
            "id": "2",
            "Nombre": "Vino",
            "Imagen": "https://img.freepik.com/vector-premium/dibujos-animados-vino-tinto-hd-contorno-color-plano_913266-667.jpg?w=2000"
        },
        {
            "id": "3",
            "Nombre": "Whisky",
            "Imagen": "https://png.pngtree.com/png-vector/20230728/ourlarge/pngtree-bourbon-clipart-whiskey-bottle-and-glass-with-iced-coffee-in-background-png-image_6804278.png"
        },
        {
            "id": "4",
            "Nombre": "Ron",
            "Imagen": "https://img.freepik.com/vector-premium/botella-ron-ilustracion-dibujos-animados-vector_574806-837.jpg"
        },
        {
            "id": "5",
            "Nombre": "Tequila",
            "Imagen": "https://previews.123rf.com/images/ofchina/ofchina1002/ofchina100200029/6466671-tequila-con-lim%C3%B3n-y-oruga.jpg"
        },
        {
            "id": "6",
            "Nombre": "Gin",
            "Imagen": "https://images.vexels.com/content/171724/preview/gin-tonic-illustration-design-6a31ab.png"
        },
        {
            "id": "7",
            "Nombre": "Vodka",
            "Imagen": "https://img.freepik.com/vector-premium/botella-vodka-ilustracion-dibujos-animados-vector_574806-835.jpg?w=2000"
        },
        {
            "id": "8",
            "Nombre": "Brandy",
            "Imagen": "https://static.vecteezy.com/system/resources/previews/014/347/695/original/bourbon-brandy-bottle-icon-cartoon-style-vector.jpg"
        },
        {
            "id": "9",
            "Nombre": "Champagne",
            "Imagen": "https://w7.pngwing.com/pngs/324/295/png-transparent-champagne-glass-sparkling-wine-champagne-bottle-s-glass-food-new-year.png"
        },
        {
            "id": "10",
            "Nombre": "Sake",
            "Imagen": "https://thumbs.dreamstime.com/b/botella-de-vidrio-sake-y-jerogl%C3%ADfico-japon%C3%A9s-ilustraci%C3%B3n-dibujos-animados-planos-color-vectorial-chopstick-bamboo-mat-187810045.jpg"
        }
    ]

    return (
        <ScrollView contentContainerStyle={styles.scrollContainer}>
            {bebidas.map((bebida) => (
                <View key={bebida.id} style={styles.container}>
                    <Image style={styles.image} source={{ uri: bebida.Imagen }} />
                    <Text style={styles.text}>{bebida.Nombre}</Text>
                </View>
            ))}
        </ScrollView>
    );
};

const styles = StyleSheet.create({
    scrollContainer: {
        paddingVertical: 20,
    },
    container: {
        flexDirection: "row",
        alignItems: "center",
        paddingHorizontal: 20,
        marginVertical: 10,
        borderWidth: 1,
        borderColor: "#ddd",
        borderRadius: 10,
        backgroundColor: "#fff",
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.2,
        shadowRadius: 3,
        elevation: 3,
    },
    image: {
        width: 80,
        height: 80,
        resizeMode: "cover",
        borderRadius: 5,
    },
    text: {
        flex: 1,
        marginLeft: 10,
        fontSize: 18,
        textAlign: "left",
        fontWeight: "bold",
        color: "#333", // color más notable
    },
});
export default Productos