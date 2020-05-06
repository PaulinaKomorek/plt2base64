import matplotlib.pyplot as plt
import base64
import io


def to_base64():
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    encoded = base64.b64encode(buf.read())
    return encoded.decode("utf-8")


plt.to_base64 = to_base64
