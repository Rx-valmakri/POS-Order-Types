/**@odoo-module **/
import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, {
       set_order_type(SelectedOrderType) {
         this.selected_order_type_id = SelectedOrderType.id;
       },
       export_as_JSON() {
          const json = super.export_as_JSON(...arguments)
          json.selected_order_Type_id = this.selected_order_type_id ;
          return json;
       }
});
