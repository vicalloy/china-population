import plotly.graph_objects as go
from plotly.subplots import make_subplots

from .utils import csv_as_list


def create_fig(data: list[list[int]]):
    fig = make_subplots(
        rows=3, cols=1, subplot_titles=("出生/死亡/增长", "入学人数", "劳动力")
    )

    # 出生/死亡/增长
    fig.add_trace(
        go.Scatter(
            x=[e[0] for e in data],
            y=[e[1] for e in data],
            mode="lines+markers+text",
            textposition="top center",
            name="出生",
            legendgroup="row1",
            showlegend=True,
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=[e[0] for e in data],
            y=[e[2] for e in data],
            mode="lines+markers+text",
            textposition="top center",
            name="死亡",
            legendgroup="row1",
            showlegend=True,
        ),
        row=1,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=[e[0] for e in data],
            y=[e[1] - e[2] for e in data],
            mode="lines+markers+text",
            textposition="top center",
            name="增长",
            legendgroup="row1",
            showlegend=True,
        ),
        row=1,
        col=1,
    )

    # 入学人数
    fig.add_trace(
        go.Scatter(
            x=[e[0] + 4 for e in data],
            y=[e[1] for e in data],
            mode="lines+markers+text",
            textposition="top center",
            name="幼儿园入学",
            legendgroup="row2",
            showlegend=True,
        ),
        row=2,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=[e[0] + 7 for e in data],
            y=[e[1] for e in data],
            mode="lines+markers+text",
            textposition="top center",
            name="小学入学",
            legendgroup="row2",
            showlegend=True,
        ),
        row=2,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=[e[0] + 18 for e in data],
            y=[e[1] for e in data],
            mode="lines+markers+text",
            textposition="top center",
            name="高考适龄",
            legendgroup="row2",
            showlegend=True,
        ),
        row=2,
        col=1,
    )

    # 劳动力
    grow: list[tuple[int, int]] = []
    for i in range(len(data) - 60 + 20):
        year = data[0][0] + 60 + i
        grow.append((year, data[60 - 20 + i][1] - data[i][1]))
    fig.add_trace(
        go.Scatter(
            x=[e[0] + 20 for e in data],
            y=[e[1] for e in data],
            mode="lines+markers+text",
            textposition="top center",
            name="新增劳动力",
            legendgroup="row3",
            showlegend=True,
        ),
        row=3,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=[e[0] + 60 for e in data],
            y=[e[1] for e in data],
            mode="lines+markers+text",
            textposition="top center",
            name="减少劳动力",
            legendgroup="row3",
            showlegend=True,
        ),
        row=3,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=[e[0] for e in grow],
            y=[e[1] for e in grow],
            mode="lines+markers+text",
            textposition="top center",
            name="劳动力增长",
            legendgroup="row3",
            showlegend=True,
        ),
        row=3,
        col=1,
    )

    fig.update_xaxes(title_text="年份")
    fig.update_yaxes(title_text="人口（万）")
    fig.update_layout(title_text="中国人口", showlegend=True)

    fig.write_html("chinapopulation.html", include_plotlyjs="cdn")


if __name__ == "__main__":
    data = [[int(e) for e in items] for items in csv_as_list("data.csv")]
    create_fig(data)
