from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Image,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime
import os

from database import get_product

def generate_invoice(

        customer,

        items,

        subtotal,

        gst,

        discount,

        grand_total

):

    if not os.path.exists("invoices"):

        os.mkdir("invoices")

    filename = f"invoices/{customer}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    invoice_no = datetime.now().strftime("INV%Y%m%d%H%M%S")

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []
    
    logo = Image(

        "company_assets/logo.png",

        width=80,

        height=80

    )

    story.append(logo)
    
    story.append(

        Paragraph(

            "<br/>",

            styles["Normal"]

        )

    )

    story.append(

        Paragraph(

            "<b><font size=22>ABC Inventory Management System</font></b>",

            styles["Title"]

        )

    )
    
    story.append(

        Paragraph(

            "Hyderabad, Telangana",

            styles["Normal"]

        )

    )

    story.append(

        Paragraph(

            "Phone : +91 9876543210",

            styles["Normal"]

        )

    )

    story.append(

        Paragraph(

            "Email : inventory@example.com",

            styles["Normal"]

        )

    )
    
    story.append(
    Paragraph(
        f"<b>Invoice No:</b> {invoice_no}",
        styles["Normal"]
    )
)

    story.append(
        Paragraph(
            f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Customer:</b> {customer}",
            styles["Normal"]
        )
    )

    story.append(

        Spacer(1,15)

    )

    story.append(

        Paragraph("<b>Purchased Products</b>", styles["Heading2"])

    )

    table_data = [

        [

            "Product",

            "Qty",
            
            "Unit Price",
            
            "Total"

        ]

    ]

    for product_name, quantity in items:

        product = get_product(product_name)

        if product:

            unit_price = float(product[3])

            quantity = int(quantity)

            total_price = unit_price * quantity

            table_data.append(

                [

                    product_name,

                    quantity,

                    f"₹ {unit_price:,.2f}",

                    f"₹ {total_price:,.2f}"

                ]

            )
    
    table = Table(

        table_data,

        colWidths=[220, 70, 120, 120]

    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("BACKGROUND",(0,1),(-1,-1),colors.beige)

        ])

    )

    story.append(table)

    story.append(

        Spacer(1,20)

    )

    story.append(

        Paragraph("<br/>", styles["Normal"])

    )

    story.append(

        Paragraph(

            f"<b>Subtotal :</b> ₹ {subtotal:.2f}",

            styles["Normal"]

        )

    )

    story.append(

        Paragraph(

            f"<b>GST :</b> ₹ {gst:.2f}",

            styles["Normal"]

        )

    )

    story.append(

        Paragraph(

            f"<b>Discount :</b> ₹ {discount:.2f}",

            styles["Normal"]

        )

    )

    story.append(

        Paragraph(

            f"<font size=14><b>Grand Total : ₹ {grand_total:.2f}</b></font>",

            styles["Heading2"]

        )

    )
    
    story.append(

        Spacer(1,20)

    )

    story.append(

        Paragraph(

            "<b>Invoice Status :</b> PAID",

            styles["Normal"]

        )

    )

    story.append(

        Paragraph(

            "<b>Payment Method :</b> Cash",

            styles["Normal"]

        )

    )

    story.append(

        Paragraph(

            "<b>GST Number :</b> 36ABCDE1234F1Z5",

            styles["Normal"]

        )

    )
    
    story.append(

        Spacer(1,40)

    )

    story.append(

        Paragraph(

            "________________________",

            styles["Normal"]

        )

    )

    story.append(

        Paragraph(

            "Authorized Signature",

            styles["Normal"]

        )

    )
    
    story.append(

        Spacer(1,20)

    )

    story.append(

        Paragraph(

            "<b>Terms & Conditions</b>",

            styles["Heading3"]

        )

    )

    story.append(

        Paragraph(

            "• Goods once sold cannot be returned.",

            styles["Normal"]

        )

    )

    story.append(

        Paragraph(

            "• Warranty is applicable only as per manufacturer policy.",

            styles["Normal"]

        )

    )

    story.append(

        Paragraph(

            "• Please keep this invoice for future reference.",

            styles["Normal"]

        )

    )

    story.append(

        Spacer(1,20)

    )

    story.append(

        Paragraph(

            "<font size=14 color='green'><b>Thank You for Your Purchase!</b></font>",

            styles["Title"]

        )

    )

    pdf.build(story)

    return filename