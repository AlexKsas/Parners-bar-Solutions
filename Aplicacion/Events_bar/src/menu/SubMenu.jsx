import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Chat from '../components/Chat/Chat';
import Home from '../components/Home/Home';
import Productos from '../components/Productos/Productos';
import InicioUser from '../components/Inicio/InicioUser';

const Tab = createBottomTabNavigator();

function SubMenu() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="InicioUser" component={InicioUser}  />
      <Tab.Screen name="Chat" component={Chat} />
      <Tab.Screen name="Productos" component={Productos} />
    </Tab.Navigator>
  );
}
export default SubMenu;