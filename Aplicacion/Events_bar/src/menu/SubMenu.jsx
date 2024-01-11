import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Chat from '../components/Chat/Chat';
import Maps from '../components/Maps/Maps';
import Productos from '../components/Productos/Productos';
import InicioUser from '../components/Inicio/InicioUser';
import { FontAwesomeIcon } from '@fortawesome/react-native-fontawesome';
import { faHome, faMap, faMessage, faMugSaucer } from '@fortawesome/free-solid-svg-icons';
import { faProductHunt } from '@fortawesome/free-brands-svg-icons';

const Tab = createBottomTabNavigator();

function SubMenu() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="home" component={InicioUser} options={{headerShown:false, tabBarIcon:({})=>(<FontAwesomeIcon icon={ faHome } />)} } />
      <Tab.Screen name="Chat" component={Chat} options={{headerShown:false,tabBarIcon:({})=>(<FontAwesomeIcon icon={ faMessage } />)}} />
      <Tab.Screen name="Productos" component={Productos} options={{headerShown:false, tabBarIcon:({})=>(<FontAwesomeIcon icon={ faProductHunt } />)}} />
      <Tab.Screen name="maps" component={Maps} options={{headerShown:false, tabBarIcon:({})=>(<FontAwesomeIcon icon={ faMap } />)}} />
    </Tab.Navigator>
  );
}
export default SubMenu;