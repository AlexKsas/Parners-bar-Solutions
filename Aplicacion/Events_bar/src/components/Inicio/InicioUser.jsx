const { Image, View, Text, StyleSheet, ScrollView } = require("react-native")

const InicioUser = () => {

    event = [
        {
            "id": "1",
            "nombre": "Rock al parque",
            "fecha": "2023-06-15",
            "lugar": "Simon Bolivar",
            "imagen": "https://colectivosonoro.com/wp-content/uploads/2019/03/rockal25.png"
        },
        {
            "id": "2",
            "nombre": "Haz Match",
            "fecha": "2023-07-22",
            "lugar": "Avenida Central 456",
            "imagen": "https://www.plans.com.mx/wp-content/uploads/2020/02/perr-1024x1024.jpg"
        },
        {
            "id": "3",
            "nombre": "Festival Cordillera",
            "fecha": "2023-08-05",
            "lugar": "Plaza del Pueblo 789",
            "imagen": "https://musicalcedar.com/wp-content/uploads/2023/08/Festival-cordillera-Musical-cedar.png"
        },
        {
            "id": "4",
            "nombre": "Techsound",
            "fecha": "2023-09-10",
            "lugar": "Calle Secundaria 321",
            "imagen": "https://urbanshadows.net/wp-content/uploads/2023/05/Techsound-Fest-foto-de-perfil.jpg"
        },
        {
            "id": "5",
            "nombre": "Estereo Picnic",
            "fecha": "2023-10-20",
            "lugar": "Avenida Principal 654",
            "imagen": "https://colectivosonoro.com/wp-content/uploads/2021/10/festival-estereo-picnic-2022-hori-2.png"
        },
        {
            "id": "6",
            "nombre": "Candelaria Rock",
            "fecha": "2023-11-12",
            "lugar": "Plaza Central 987",
            "imagen": "https://bogota.gov.co/sites/default/files/styles/1050px/public/eventos/2023-08/rock-en-la-media-torta.jpeg"
        },
        {
            "id": "7",
            "nombre": "Monster Of Rock",
            "fecha": "2023-12-08",
            "lugar": "Calle Principal 147",
            "imagen": "https://www.autopistarock.com/images/easyblog_articles/5968/b2ap3_large_PosterMonstersAngraF.jpeg"
        },
        {
            "id": "8",
            "nombre": "Knofest",
            "fecha": "2023-09-30",
            "lugar": "Avenida Central 258",
            "imagen": "https://cdn.puntoticket.com/especiales/knt001_knotfest/img/knotfest-mov-v2.jpg"
        },
        {
            "id": "9",
            "nombre": "Deluxe Night",
            "fecha": "2023-07-17",
            "lugar": "Plaza del Pueblo 369",
            "imagen": "https://www.tropopublicidad.com/fotos/prj_32/2/8/img-28_28-s-1602377193.jpg"
        },
        {
            "id": "10",
            "nombre": "Nigth Party",
            "fecha": "2023-08-28",
            "lugar": "Calle Secundaria 753",
            "imagen": "https://www.tropopublicidad.com/fotos/prj_32/3/2/img-32_32-s-1602377869.jpg"
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
            color:'gray'
        },
        eventLocation: {
            fontSize: 16,
            color:'gray'
        },
        eventDate: {
            fontSize: 16,
            color:'gray'
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