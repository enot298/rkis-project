import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import OrderDetailScreen from "../screens/OrderDetailScreen";
import OrderFormScreen from "../screens/OrderFormScreen";
import OrderListScreen from "../screens/OrderListScreen";
import { colors } from "../theme/tokens";

const Stack = createNativeStackNavigator();

// Стековая навигация: список -> детали / форма (схема: design/mockups/mobile-nav.svg)
export default function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="OrderList"
        screenOptions={{
          headerStyle: { backgroundColor: colors.surface },
          headerTintColor: colors.text,
        }}
      >
        <Stack.Screen name="OrderList" component={OrderListScreen} options={{ title: "Заказы" }} />
        <Stack.Screen name="OrderDetail" component={OrderDetailScreen} options={{ title: "Заказ" }} />
        <Stack.Screen name="OrderForm" component={OrderFormScreen} options={{ title: "Новый заказ" }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
