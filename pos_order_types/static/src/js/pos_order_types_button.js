/**@odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";


export class OrderTypesButton extends Component {
     static template = "point_of_sale.OrderTypesButton";

     setup() {
        this.pos = usePos();
    	this.popup = useService("popup");
    	this.pos.is_order_type_pop_up = false;
	}

	async onClick() {
	    var order_types = []
	    var order_type_in_settings = eval(this.pos.pos_order_types[1])
	    for (var i=0; i<this.pos.pos_order_types[0].length; i++)
	    {
	       if (order_type_in_settings.includes(this.pos.pos_order_types[0][i].id))
	       {
	          order_types.push(this.pos.pos_order_types[0][i])
	       }
	    }
	    const { confirmed, payload: SelectedOrderType } = await this.popup.add(SelectionPopup, {
        	title: ('Choose Order Type'),
            list: order_types.map((order_type) => ({
                        id: order_type.id,
                        item: order_type,
                        label: order_type.name,
                    })),
    	});
    	if (confirmed)
    	{
    	  this.pos.get_order().selected_order_type = SelectedOrderType
    	  this.pos.get_order().set_order_type(SelectedOrderType)
    	  this.pos.is_order_type_pop_up = true
    	}
	}

}
ProductScreen.addControlButton({
    component: OrderTypesButton,
    position: ["after", "point_of_sale.OrderWidget"],
    condition: function () {
          return this.pos.pos_order_types[0][0].is_pos_settings_enabled && eval(this.pos.pos_order_types[1]).length > 0;
      },
});
