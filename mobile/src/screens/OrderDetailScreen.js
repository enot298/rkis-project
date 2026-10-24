import { StyleSheet, View } from "react-native";

import Button from "../components/Button";
import ScreenTitle from "../components/ScreenTitle";
import { colors, space } from "../theme/tokens";

// Экран-заглушка: детали заказа
export default function OrderDetailScreen({ navigation, route }) {
  const orderId = route.params?.orderId;
  return (
    <View style={styles.screen}>
      <ScreenTitle title={`Заказ № ${orderId ?? "—"}`} subtitle="Детали заказа. Заглушка." />
      <Button title="Назад к списку" variant="secondary" onPress={() => navigation.goBack()} />
    </View>
  );
}

const styles = StyleSheet.create({
  screen: { flex: 1, padding: space.s4, backgroundColor: colors.background },
});
