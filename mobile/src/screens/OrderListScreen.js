import { StyleSheet, View } from "react-native";

import Button from "../components/Button";
import ScreenTitle from "../components/ScreenTitle";
import { colors, space } from "../theme/tokens";

// Экран-заглушка: список заказов
export default function OrderListScreen({ navigation }) {
  return (
    <View style={styles.screen}>
      <ScreenTitle title="Заказы" subtitle="Список заказов. Данные появятся на этапе Э9." />
      <View style={styles.actions}>
        <Button
          title="Открыть заказ (пример)"
          variant="secondary"
          onPress={() => navigation.navigate("OrderDetail", { orderId: 1 })}
        />
        <Button title="Новый заказ" onPress={() => navigation.navigate("OrderForm")} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  screen: { flex: 1, padding: space.s4, backgroundColor: colors.background },
  actions: { gap: space.s3 },
});
