const { Image, View, Text, StyleSheet, ScrollView } = require("react-native")

const InicioUser = () => {

    event = [
        {
            "id": "1",
            "nombre": "Rock al parque",
            "fecha": "2023-06-15",
            "lugar": "Simon Bolivar",
            "imagen": "data:image/png;base64,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"
        },
        {
            "id": "2",
            "nombre": "Proyecto X",
            "fecha": "2023-07-22",
            "lugar": "Avenida Central 456",
            "imagen": "data:image/jpeg;base64,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"
        },
        {
            "id": "3",
            "nombre": "Festival de Cervezas",
            "fecha": "2023-08-05",
            "lugar": "Plaza del Pueblo 789",
            "imagen": "https://png.pngtree.com/png-clipart/20190515/original/pngtree-summer-midsummer-beer-celebrate-png-image_3779777.jpg"
        },
        {
            "id": "4",
            "nombre": "Noche de Vinos",
            "fecha": "2023-09-10",
            "lugar": "Calle Secundaria 321",
            "imagen": "https://png.pngtree.com/png-clipart/20190515/original/pngtree-summer-midsummer-beer-celebrate-png-image_3779777.jpg"
        },
        {
            "id": "5",
            "nombre": "Fiesta de la Vendimia",
            "fecha": "2023-10-20",
            "lugar": "Avenida Principal 654",
            "imagen": "https://png.pngtree.com/png-clipart/20190515/original/pngtree-summer-midsummer-beer-celebrate-png-image_3779777.jpg"
        },
        {
            "id": "6",
            "nombre": "Festival de Tequila",
            "fecha": "2023-11-12",
            "lugar": "Plaza Central 987",
            "imagen": "https://png.pngtree.com/png-clipart/20190515/original/pngtree-summer-midsummer-beer-celebrate-png-image_3779777.jpg"
        },
        {
            "id": "7",
            "nombre": "Cata de Whisky",
            "fecha": "2023-12-08",
            "lugar": "Calle Principal 147",
            "imagen": "https://png.pngtree.com/png-clipart/20190515/original/pngtree-summer-midsummer-beer-celebrate-png-image_3779777.jpg"
        },
        {
            "id": "8",
            "nombre": "Fiesta de la Cerveza",
            "fecha": "2023-09-30",
            "lugar": "Avenida Central 258",
            "imagen": "https://png.pngtree.com/png-clipart/20190515/original/pngtree-summer-midsummer-beer-celebrate-png-image_3779777.jpg"
        },
        {
            "id": "9",
            "nombre": "Noche de Cocteles",
            "fecha": "2023-07-17",
            "lugar": "Plaza del Pueblo 369",
            "imagen": "https://png.pngtree.com/png-clipart/20190515/original/pngtree-summer-midsummer-beer-celebrate-png-image_3779777.jpg"
        },
        {
            "id": "10",
            "nombre": "Festival de Vinos",
            "fecha": "2023-08-28",
            "lugar": "Calle Secundaria 753",
            "imagen": "https://png.pngtree.com/png-clipart/20190515/original/pngtree-summer-midsummer-beer-celebrate-png-image_3779777.jpg"
        }
    ]
    const styles = StyleSheet.create({
        container: {
            margin: 10,
            padding: 10,
            backgroundColor: 'white',
            borderRadius: 10,
            shadowColor: '#000',
            shadowOffset: {
                width: 0,
                height: 2,
            },
            shadowOpacity: 0.25,
            shadowRadius: 3.84,
            elevation: 5,
        },
        image: {
            width: '100%',
            height: 200,
            resizeMode: 'cover',
            borderRadius: 8,
        },
        textContainer: {
            flexDirection: 'row',
            justifyContent: 'space-between',
            marginTop: 10,
        },
        eventName: {
            fontSize: 20,
            fontWeight: 'bold',
        },
        eventLocation: {
            fontSize: 16,
        },
        eventDate: {
            fontSize: 16,
        },
    })

    return (
        <ScrollView>
            {event.map((event) => (
                <View key={event.id} style={styles.container}>
                    <Image style={styles.image} source={{ uri: event.imagen }} />
                    <View style={styles.textContainer}>
                        <Text style={styles.eventName}>{event.nombre}</Text>
                        <Text style={styles.eventDate}>{event.fecha}</Text>
                    </View>
                    <Text style={styles.eventLocation}>{event.lugar}</Text>
                </View>
            ))}
        </ScrollView>
    )
}

export default InicioUser