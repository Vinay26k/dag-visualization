import json
import jinja2
import shutil, os


def graph_parser(graph_dict: dict):
    node_repr_json = {}
    for each_node in graph_dict["nodes"]:
        # json_parsable_graph.append(each_node)
        node_repr_json[each_node["id"]] = each_node

    # change name label to products for now
    for each_node in node_repr_json:
        # json_parsable_graph.append(each_node)
        node_repr_json[each_node]["products"] = (
            node_repr_json[each_node]["label"].replace("\n", "").split(",")
        )

    for each_link in graph_dict["links"]:
        existing_vals = node_repr_json[each_link["source"]].get("parentIds", [])
        existing_vals.append(each_link["target"])
        node_repr_json[each_link["source"]]["parentIds"] = existing_vals

    # print(list(node_repr_json.values()))
    return json.dumps(list(node_repr_json.values()))


def gen_plot(graph_dict):
    print("executing gen_plot")
    template = jinja2.Template(open("dag.html").read())
    updated = template.render({"json_data": graph_parser(graph_dict=graph_dict)})
    with open("out.html", "w") as f:
        f.write(updated)


## graph dict generated from ploomber ml-basic sample
graph_dict = {
    "directed": True,
    "multigraph": False,
    "graph": {},
    "nodes": [
        {
            "color": "green",
            "id": "get",
            "label": "get -> \nFile('output\\\\get.pa\nrquet')\n",
        },
        {
            "color": "green",
            "id": "features",
            "label": "features -> \nFile('output\\\\featur\nes.parquet')\n",
        },
        {
            "color": "green",
            "id": "join",
            "label": "join -> \nFile('output\\\\join.p\narquet')\n",
        },
        {
            "color": "green",
            "id": "fit",
            "label": "fit -> \nFile('output\\\\nb.ipy\nnb')\n, File('output\\\\model.\npickle')\n",
        },
    ],
    "links": [
        {"source": "get", "target": "features"},
        {"source": "get", "target": "join"},
        {"source": "features", "target": "join"},
        {"source": "join", "target": "fit"},
    ],
}


gen_plot(graph_dict=graph_dict)
