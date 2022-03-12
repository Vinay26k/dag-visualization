function get_node_product_rectangle(align) {
    if (align == "left") {
      return "translate(3, 6)";
    } else {
      return "translate(-50, 6)";
    }
  }
  
  function get_node_product_text(n_products, align) {
    n_products = n_products < 2 ? 2 : n_products;
    if (align == "left") {
      return "translate(5," + 16 / n_products + ")";
    } else {
      return "translate(-50, " + 16 / n_products + ")";
    }
  }
  
  function products_len(d, default_val, thresh) {
    if (d.data.products != undefined && d.data.products.length > thresh) {
      return d.data.products.length;
    }
    return default_val;
  }
  
  function get_node_props(node, align) {
    // products
    var node_props = {};
    node_props["align"] = align;
    node_props["n_products"] = 0;
    node_props["product_width"] = 30;
    node_props["product_height"] = 6;
  
    if ("products" in node.data && node.data.products.length != 0) {
      console.log(
        node.data.id,
        node.data.products,
        node.data.products.length,
        "success"
      );
      node_props["n_products"] = node.data.products.length;
      node_props["product_width"] *=
        node_props["n_products"] < 2 ? 2 : node_props["n_products"];
      node_props["product_height"] *= node_props["n_products"];
      // node_props["product_display"] = "block";
    } else {
      node_props["product_display"] = "contents";
    }
    node_props["product_rect_align"] = get_node_product_rectangle(align);
    node_props["product_text_align"] = get_node_product_text(
      node_props["n_products"],
      align
    );
  
    return node_props;
  }
  
  function get_dag_render_props(dag) {
    var dag_render_props = {};
    dag_render_props[dag.data.id] = get_node_props(dag, "left");
  
    cNodes = dag.descendants();
  
    for (var eNode in cNodes) {
      for (var ec in cNodes[eNode].children()) {
        // tmp props
  
        var align = ec % 2 ? "right" : "left";
  
        dag_render_props[cNodes[eNode].children()[ec].data.id] = get_node_props(
          cNodes[eNode].children()[ec],
          align
        );
      }
    }
    return dag_render_props;
  }
  