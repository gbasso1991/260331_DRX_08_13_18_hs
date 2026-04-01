<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html xmlns:v="urn:schemas-microsoft-com:vml">
            <head>
                <style>
                    v\:*{behavior:url(#default#VML);}&gt;
                </style>
            </head>

            <body bgcolor="lightblue">
                <table border="0" width="75%" align="center">
                    <tr>
                        <td align="center">
                            <br>
                            </br>

                            <br>
                            </br>

                            <table border="0">
                                <tr>
                                    <td align="center">
                                        <h2>PDF Card</h2>
                                    </td>
                                </tr>
                            </table>

                            <table border="1">
                                <xsl:for-each select="pdfcard/pdf_data">
                                    <tr>
                                        <td>
                                            <b>PDF Number</b>
                                        </td>

                                        <td colspan="2">
                                            <xsl:value-of select="pdf_number" />
                                        </td>

                                        <td>
                                            <b>Status</b>

                                            <br>
                                            </br>
                                        </td>

                                        <td>
                                            <xsl:value-of select="status" />
                                        </td>

                                        <td colspan="2">
                                            <b>Quality Mark</b>
                                        </td>

                                        <td>
                                            <xsl:value-of select="quality_mark" />
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Pressure/Temperature</b>
                                        </td>

                                        <td colspan="7">
                                            <xsl:value-of select="pressure_temperature" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
									
									<tr>
                                        <td>
                                            <b>Phase</b>
                                        </td>

                                        <td colspan="7">
                                            <xsl:value-of select="phase" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Chemical Formula</b>
                                        </td>

                                        <td colspan="7">
                                            <xsl:value-of select="chemical_formula" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
                           
                                    <tr>
                                        <td>
                                            <b>Structural Formula</b>
                                        </td>

                                        <td colspan="7">
											<font face="Arial Greek"><xsl:value-of select="structural_formula" /></font>

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Empirical Formula</b>
                                        </td>

                                        <td colspan="7">
                                            <xsl:value-of select="empirical_formula" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Weight %</b>
                                        </td>

                                        <td colspan="7">
                                            <xsl:value-of select="weight_percent" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
                           
                                    <tr>
                                        <td>
                                            <b>Atomic %</b>
                                        </td>

                                        <td colspan="7">
                                            <xsl:value-of select="atomic_percent" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
                           
                                    <tr>
                                        <td>
                                            <b>Compound Name</b>
                                        </td>

                                        <td colspan="7">
                                            <font face="Arial Greek"><xsl:value-of select="chemical_name" /></font>

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Mineral Name</b>
                                        </td>

                                        <td colspan="7">
                                            <xsl:value-of select="mineralname" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Common Name</b>
                                        </td>

                                        <td colspan="7">
                                            <font face="Arial Greek"><xsl:value-of select="commonname" /></font>

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
									
                                    <tr>
                                        <td>
                                            <b>CAS Number</b>
                                        </td>

                                        <td colspan="7">
                                            <font face="Arial Greek"><xsl:value-of select="cas" /></font>

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
									
									<tr>
                                        <td>
                                            <b>Entry Date</b>
                                        </td>

                                        <td colspan="7">
                                            <font face="Arial Greek"><xsl:value-of select="entry_date" /></font>

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
                           
                                    <tr>
                                        <td>
                                            <b>Last Modification Date</b>
                                        </td>

                                        <td colspan="7">
                                            <font face="Arial Greek"><xsl:value-of select="last_mod_date" /></font>

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
                           
                                    <tr>
                                        <td>
                                            <b>Last Modifications</b>
                                        </td>

                                        <td colspan="7">
                                            <font face="Arial Greek"><xsl:value-of select="last_modifications" /></font>

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
									
                                </xsl:for-each>

                                <xsl:for-each select="pdfcard/pdf_data">
                                    <tr>
                                        <td rowspan="4"><font size="4"><b>Experimental</b></font></td>
                                        <td><b>Rad</b></td>
                                        <td><b><font face="symbol">l</font></b></td>
                                        <td><b>Filter</b></td>
                                        <td><b>d-Spacing</b></td>
                                        <td><b>Cutoff</b></td>
                                        <td><b>Intensity</b></td>
                                        <td><b>I/Ic</b></td>
                                    </tr>
                                    <tr>
                                        <td><font face="Arial Greek"><xsl:value-of select="patrad" /><br></br></font></td>
                                        <td><xsl:value-of select="lambda" /><br></br></td>
                                        <td><xsl:value-of select="filttyp" /><br></br></td>
                                        <td><xsl:value-of select="instrument" /><br></br></td>
                                        <td><xsl:value-of select="lower" /><br></br></td>
                                        <td><xsl:value-of select="source" /><br></br></td>
                                        <td><xsl:value-of select="iic" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td><b>I/Ic - ND</b></td>
										<td><b>Camera Diameter</b></td>
										<td><b>Internal Standard</b></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="iic_nd" /><br></br></td>
										<td><xsl:value-of select="diameter" /><br></br></td>
										<td><xsl:value-of select="internal_standard" /><br></br></td>
                                    </tr>

                                    <tr>
                                        <td rowspan="13"><font size="4"><b>Physical</b></font></td>
                                        <td><b>SYS</b></td>
                                        <td><b><xsl:value-of select="spgr_label" /></b></td>
                                        <td><b>Aspect</b></td>
										<td><b>Modulation Wave Vectors</b></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="xstal_system" /><br></br></td>
                                        <td><font face="Arial Greek"><xsl:value-of select="spgr" /></font><br></br></td>
                                        <td><xsl:value-of select="spgraspect" /><br></br></td>
                                        <td colspan="6">
                                            <table border="1">
                                                <xsl:for-each select="mod_wave_vectors/mod_wave_vector_row">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="mod_wave_vector"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr> 
                                        <td>
                                            <b>Subsystems</b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>ID</td>
                                                    <td>W Matrix</td>
                                                </tr>
                                                <xsl:for-each select="subsystems/subsystem">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="subsystem_id"/>
                                                        </td>
                                                        <td>
															<table border="1">
																<xsl:for-each select="w_matrix/w_matrix_row">
																	<tr>
																		<td>
																			<xsl:value-of select="."/>
																		</td>
																	</tr>
																</xsl:for-each>
															</table>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td rowspan="4"><b>Author's Cell</b></td>
                                        <td><b>a</b></td>
                                        <td><b>b</b></td>
                                        <td><b>c</b></td>
                                        <td><font face="symbol"><b>a</b></font></td>
                                        <td><font face="symbol"><b>b</b></font></td>
                                        <td><font face="symbol"><b>g</b></font></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="cell_a" /><br></br></td>
                                        <td><xsl:value-of select="cell_b" /><br></br></td>
                                        <td><xsl:value-of select="cell_c" /><br></br></td>
                                        <td><xsl:value-of select="cell_alpha" /><br></br></td>
                                        <td><xsl:value-of select="cell_beta" /><br></br></td>
                                        <td><xsl:value-of select="cell_gamma" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td><b>Volume</b></td>
										<td><b>Z</b></td>
										<td><b>Molecular Volume/Formula Unit Volume</b></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="cell_vol" /><br></br></td>
										<td><xsl:value-of select="z" /><br></br></td>
										<td><xsl:value-of select="cell_mv" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2"><b>Author's Cell Axial Ratio</b></td>
                                        <td><b>c/a</b></td>
                                        <td><b>a/b</b></td>
										<td><b>c/b</b></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="authcovera" /><br></br></td>
                                        <td><xsl:value-of select="authaoverb" /><br></br></td>
										<td><xsl:value-of select="authcoverb" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2"><b>Density</b></td>
                                        <td><b>Dcalc</b></td>
                                        <td><b>Dmeas</b></td>
										<td><b>Dstruc</b></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="xtldx" /><br></br></td>
                                        <td><xsl:value-of select="dm" /><br></br></td>
										<td><xsl:value-of select="ds" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td><b>SS/FOM</b></td>
                                        <td><b>Temperature</b></td>
										<td><b>Melting Point</b></td>
                                        <td><b>R-factor</b></td>
										<td><b>Error</b></td>
										<td><b>Color</b></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="ss" /><br></br></td>
                                        <td><xsl:value-of select="temperature" /><br></br></td>
										<td><xsl:value-of select="melting_points" /><br></br></td>
                                        <td><xsl:value-of select="rfactor" /><br></br></td>
										<td><xsl:value-of select="error" /><br></br></td>
										<td><xsl:value-of select="color" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td rowspan="13"><font size="4"><b>Crystal</b></font></td>
                                        <td><b>Space Group</b></td>
                                        <td><b>Molecular Weight</b></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="xtlsg" /><br></br></td>
                                        <td><xsl:value-of select="xtlmolwt" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td rowspan="4"><b>Crystal Data</b></td>
                                        <td><b>a</b></td>
                                        <td><b>b</b></td>
                                        <td><b>c</b></td>
                                        <td><font face="symbol"><b>a</b></font></td>
                                        <td><font face="symbol"><b>b</b></font></td>
                                        <td><font face="symbol"><b>g</b></font></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="xtla" /><br></br></td>
                                        <td><xsl:value-of select="xtlb" /><br></br></td>
                                        <td><xsl:value-of select="xtlc" /><br></br></td>
                                        <td><xsl:value-of select="xtlal" /><br></br></td>
                                        <td><xsl:value-of select="xtlbe" /><br></br></td>
                                        <td><xsl:value-of select="xtlga" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td><b>Volume</b></td>
										<td><b>Z</b></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="xtlvol" /><br></br></td>
										<td><xsl:value-of select="xtlz" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2"><b>Crystal Data Axial Ratio</b></td>
                                        <td><b>c/a</b></td>
                                        <td><b>a/b</b></td>
										<td><b>c/b</b></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="xtlcovera" /><br></br></td>
                                        <td><xsl:value-of select="xtlaoverb" /><br></br></td>
										<td><xsl:value-of select="xtlcoverb" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td rowspan="5"><b>Reduced Cell</b></td>
                                        <td><b>a</b></td>
                                        <td><b>b</b></td>
                                        <td><b>c</b></td>
                                        <td><font face="symbol"><b>a</b></font></td>
                                        <td><font face="symbol"><b>b</b></font></td>
                                        <td><font face="symbol"><b>g</b></font></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="redcell_a" /><br></br></td>
                                        <td><xsl:value-of select="redcell_b" /><br></br></td>
                                        <td><xsl:value-of select="redcell_c" /><br></br></td>
                                        <td><xsl:value-of select="redcell_al" /><br></br></td>
                                        <td><xsl:value-of select="redcell_be" /><br></br></td>
                                        <td><xsl:value-of select="redcell_ga" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td><b>Volume</b></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="redcellvol" /><br></br></td>
                                    </tr>
                                    <tr>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td><xsl:value-of select="metric_symmetry_warning"/></td>
                                                </tr>
                                                <xsl:for-each select="metric_symmetry_warning_comments/metric_symmetry_warning_comment_group">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="metric_symmetry_warning_comment"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td rowspan="2"><font size="4"><b>Optical</b></font></td>
                                        <td><b><font face="symbol">e</font><font face="symbol">a</font></b></td>
                                        <td><b>n<font face="symbol">w</font><font face="symbol">b</font></b></td>
                                        <td><b><font face="symbol">e</font><font face="symbol">g</font></b></td>
                                        <td><b>Sign</b></td>
                                        <td><b>2V</b></td>
                                    </tr>
                                    <tr>
                                        <td><xsl:value-of select="optical_data_alpha" /><br></br></td>
                                        <td><xsl:value-of select="optical_data_beta" /><br></br></td>
                                        <td><xsl:value-of select="optical_data_gamma" /><br></br></td>
                                        <td><xsl:value-of select="optical_data_sign" /><br></br></td>
                                        <td><xsl:value-of select="optical_data_2v" /><br></br></td>
                                    </tr>
                                </xsl:for-each>

                                <xsl:for-each select="pdfcard/pdf_data">
                                    <tr>
                                        <td rowspan="10">
                                            <font size="4">
                                                <b>Structure</b>
                                            </font>
                                        </td>

                                        <td colspan="7">
                                            <xsl:value-of select="structure_info"/>
                                            <br></br>
                                        </td>
                                    </tr>
                             
                                    <tr> 
                                        <td>
                                            <b>ADP Type</b>
                                        </td>
                              
                                        <td colspan="6">
                                            <xsl:value-of select="tf_type"/>
                                            <br></br>
                                        </td>
                                    </tr>

                                    <tr> 
                                        <td>
                                            <b>Origin</b>
                                        </td>
                              
                                        <td colspan="6">
                                            <xsl:value-of select="origin"/>
                                            <br></br>
                                        </td>
                                    </tr>

                                    <tr> 
                                        <td>
                                            <b>Crystal (Symmetry Allowed)</b>
                                        </td>
                              
                                        <td colspan="6">
                                            <xsl:value-of select="crystal_properties"/>
                                            <br></br>
                                        </td>
                                    </tr>

                                    <tr> 
                                        <td>
                                            <b>SG Symmetry Operators</b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Seq</td>
                                                    <td>Operator</td>
                                                </tr>
                                                <xsl:for-each select="sg_sym_ops/sg_sym_op">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="seq"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="operator"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>
                           
                                    <tr> 
                                        <td>
                                            <b>SG Symmetry Operators (Modulated Structure)</b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Seq</td>
                                                    <td>Operator</td>
                                                </tr>
                                                <xsl:for-each select="sg_sym_ops_mod/sg_sym_op">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="seq"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="operator"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>

                                    <tr> 
                                        <td>
                                            <b>Atomic Coordinates</b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Atom</td>
                                                    <td>Num</td>
                                                    <td>Wyckoff</td>
                                                    <td>Symmetry</td>
                                                    <td>x</td>
                                                    <td>y</td>
                                                    <td>z</td>
                                                    <td>SOF</td>
                                                    <td><xsl:value-of select="idp_column"/></td>
                                                    <td>AET</td>
                                                </tr>
                                                <xsl:for-each select="atomic_coords/atomic_coord">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="atom"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="num"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <font face="Arial Greek"><xsl:value-of select="wyckoff"/></font>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="symmetry"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="x"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="y"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="z"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="sof"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="idp"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="aet"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>
                           
                                    <tr> 
                                        <td>
                                            <b>Atomic Coordinates (Modulated)</b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Atom</td>
                                                    <td>Num</td>
													<td>Wyckoff</td>
                                                    <td>x</td>
                                                    <td>y</td>
                                                    <td>z</td>
                                                    <td>SOF</td>
                                                    <td><xsl:value-of select="idp_column"/></td>
													<td>Subsys</td>
                                                </tr>
                                                <xsl:for-each select="atomic_coords_mod/atomic_coord">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="atom"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="num"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="wyckoff"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="x"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="y"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="z"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="sof"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="idp"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="subsys_id"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>
									
                                    <tr> 
                                        <td>
                                            <b>Anisotropic Displacement Parameters</b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Atom</td>
                                                    <td>Num</td>
                                                    <td><xsl:value-of select="adp_column"/>11</td>
                                                    <td><xsl:value-of select="adp_column"/>22</td>
                                                    <td><xsl:value-of select="adp_column"/>33</td>
                                                    <td><xsl:value-of select="adp_column"/>12</td>
                                                    <td><xsl:value-of select="adp_column"/>13</td>
                                                    <td><xsl:value-of select="adp_column"/>23</td>
                                                </tr>
                                                <xsl:for-each select="ani_temp_facs/ani_temp_fac">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="atom"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="num"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp11"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp22"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp33"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp12"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp13"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp23"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>
                           
                                    <tr> 
                                        <td>
                                            <b>Anisotropic Displacement Parameters (Modulated) </b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Atom</td>
                                                    <td>Num</td>
                                                    <td><xsl:value-of select="adp_column"/>11</td>
                                                    <td><xsl:value-of select="adp_column"/>22</td>
                                                    <td><xsl:value-of select="adp_column"/>33</td>
                                                    <td><xsl:value-of select="adp_column"/>12</td>
                                                    <td><xsl:value-of select="adp_column"/>13</td>
                                                    <td><xsl:value-of select="adp_column"/>23</td>
                                                </tr>
                                                <xsl:for-each select="ani_temp_facs_mod/ani_temp_fac">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="atom"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="num"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp11"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp22"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp33"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp12"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp13"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="adp23"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>
									
                                    <tr>
                                        <td rowspan="6">
                                            <font size="4">
                                                <b>Modulated</b>
                                            </font>
                                        </td>

                                    <tr> 
                                        <td>
                                            <b>Positional Displacement Parameters</b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Atom Site</td>
                                                    <td>Axis</td>
                                                    <td>WV ID</td>
                                                    <td>Cos</td>
                                                    <td>Sin</td>
                                                </tr>
                                                <xsl:for-each select="positional_displacement_params/positional_displacement_param">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="atom_site"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="axis"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="wv_id"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="cos"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="sin"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>

                                    <tr> 
                                        <td>
                                            <b>Atomic Displacement Parameters</b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Atom Site</td>
                                                    <td>WV ID</td>
                                                    <td>Cos</td>
													<td>Sin</td>
                                                    <td>Tensor El.</td>
                                                </tr>
                                                <xsl:for-each select="atomic_displacement_params/atomic_displacement_param">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="atom_site"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="wv_id"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="cos"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="sin"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="tensor_element"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>

                                    <tr> 
                                        <td>
                                            <b>Occupation Modulation</b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Atom Site</td>
													<td>WV ID</td>
                                                    <td>Cos</td>
													<td>Sin</td>
                                                </tr>
                                                <xsl:for-each select="occupation_modulations/occupation_modulation">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="atom_site"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="wv_id"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="cos"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="sin"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>

                                    <tr> 
                                        <td>
                                            <b>Occupational - Crenel</b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Atom Site</td>
													<td>C</td>
                                                    <td>W</td>
                                                </tr>
                                                <xsl:for-each select="crenel_functions/crenel_function">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="atom_site"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="crenel_c"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="crenel_w"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>
									
                                    <tr> 
                                        <td>
                                            <b>Displacement - SawTooth</b>
                                        </td>
                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Atom Site</td>
													<td>C</td>
                                                    <td>W</td>
													<td>AX</td>
													<td>AY</td>
													<td>AZ</td>
                                                </tr>
                                                <xsl:for-each select="sawtooth_functions/sawtooth_function">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="atom_site"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="sawtooth_c"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="sawtooth_w"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="ax"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="ay"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="az"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>

                                    </tr>

                                    <tr>
                                        <td rowspan="10">
                                            <font size="4">
                                                <b>Classifications</b>
                                            </font>
                                        </td>

                                        <td>
                                            <b>Subfiles</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="subfile_indicator" />
                                            <br></br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Mineral Classification</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="pdf_minclass" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
                           
                                    <tr>
                                        <td>
                                            <b>Zeolite Classification</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="pdf_zeoclass" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
                           
                                    <tr>
                                        <td>
                                            <b>Pearson</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="pearson" />
                                            <br></br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Pearson w/o H</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="pearson_without_h" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Prototype Structure</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="rep_struc" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Prototype Structure (Alpha Sort)</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="rep_struc_alpha_sort" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>LPF Prototype Structure</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="lpf_rep_struc" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>LPF Prototype Structure (Alpha Sort)</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="lpf_rep_struc_alpha_sort" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
									
									<tr>
                                        <td>
                                            <b>ANX</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="anx" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td rowspan="2">
                                            <font size="4">
                                                <b>Cross-references</b>
                                            </font>
                                        </td>

                                        <td>
                                            <b>Cross-references</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="cross_ref_pdf_numbers" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Former PDF Numbers</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="former_pdf_number" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <font size="4">
                                                <b>References</b>
                                            </font>
                                        </td>

                                        <td colspan="6">
                                            <table border="1">
                                                <tr bgcolor="#9acd32">
                                                    <td>Type</td>
													<td>DOI</td>
                                                    <td>Reference</td>
                                                </tr>
                                                <xsl:for-each select="references/reference_group">
                                                    <tr>
                                                        <td>
                                                            <xsl:value-of select="type"/>
                                                            <br></br>
                                                        </td>
                                                        <td>
															<xsl:element name="a"><xsl:attribute name="href"><xsl:text>http://dx.doi.org/</xsl:text><xsl:value-of select="doi"/></xsl:attribute><xsl:value-of select="doi"/></xsl:element>                                                            
                                                            <br></br>
                                                        </td>
                                                        <td>
                                                            <xsl:value-of select="reference"/>
                                                            <br></br>
                                                        </td>
                                                    </tr>
                                                </xsl:for-each>
                                            </table>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td rowspan="3">
                                            <font size="4">
                                                <b>Comments</b>
                                            </font>
                                        </td>

                                        <td>
                                            <b>Database Comments</b>
                                        </td>

                                        <td colspan="6">
                                            <font face="Arial Greek"><xsl:value-of select="database_comments" /></font>

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>User Comments</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="user_comments" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>
                                            <b>Shared Comments</b>
                                        </td>

                                        <td colspan="6">
                                            <xsl:value-of select="shared_comments" />

                                            <br>
                                            </br>
                                        </td>
                                    </tr>
                                </xsl:for-each>
                            </table>

                            <br></br>
                            <br></br>

                            <table border="0">
                                <tr>
                                    <td align="center">
                                        <h2>d-Spacings</h2>
                                    </td>
                                </tr>
				
                                <tr>
                                    <td align="center">
                                        <b>
                                        <font face="symbol">l</font>
                                        =</b>
                                        <xsl:value-of select="pdfcard/graphs/wave_length" />
                                    </td>  
                                </tr>
                            </table>
				
                            <center><img>
                                <xsl:attribute name="src">
                                    <xsl:value-of select="pdfcard/graphs/chart_name" />
                                </xsl:attribute>
                            </img></center>

                            <br></br>
                            <br></br>

                            <xsl:for-each select="pdfcard/graphs/stick_series">
                                <h2><xsl:value-of select="@type"/></h2>
                                <table border="1">
                                    <tr bgcolor="#9acd32">
                                        <td>2<font face="symbol">q</font></td>
                                        <td>d(Å)</td>
                                        <td>Intensity</td>
                                        <td>h</td>
                                        <td>k</td>
                                        <td>l</td>
										<td>m</td>
										<td>n</td>
										<td>o</td>
                                        <td>*</td>
                                    </tr>

                                    <xsl:for-each select="intensity">
                                        <tr>
                                            <td>
                                                <xsl:value-of select="theta" />
                                                <br>
                                                </br>
                                            </td>
                                            <td>
                                                <xsl:value-of select="da" />
                                                <br>
                                                </br>
                                            </td>
                                            <td>
                                                <xsl:value-of select="intensity" />
                                                <br>
                                                </br>
                                            </td>
                                            <td>
                                                <xsl:value-of select="h" />
                                                <br>
                                                </br>
                                            </td>
                                            <td>
                                                <xsl:value-of select="k" />
                                                <br>
                                                </br>
                                            </td>
                                            <td>
                                                <xsl:value-of select="l" />
                                                <br>
                                                </br>
                                            </td>
                                            <td>
                                                <xsl:value-of select="M1"/>
                                                <br>
                                                </br>
                                            </td>
                                            <td>
                                                <xsl:value-of select="M2"/>
                                                <br>
                                                </br>
                                            </td>
                                            <td>
                                                <xsl:value-of select="M3"/>
                                                <br>
                                                </br>
                                            </td>
                                            <td>
                                                <sup><xsl:value-of select="F" /></sup>
                                                <br>
                                                </br>
                                            </td>
                                        </tr>
                                    </xsl:for-each>
                                </table>
                            </xsl:for-each>

                            <br></br>
                            <xsl:for-each select="pdfcard">
                                <copy_right>© 2013 International Centre for Diffraction Data. All Rights Reserved</copy_right>
                            </xsl:for-each>
                        </td>
                    </tr>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>

<!-- Stylus Studio meta-information - (c)1998-2004. Sonic Software Corporation. All rights reserved.
<metaInformation>
<scenarios ><scenario default="yes" name="Scenario1" userelativepaths="yes" externalpreview="no" url="pdf2.xml" htmlbaseurl="" outputurl="" processortype="internal" profilemode="0" profiledepth="" profilelength="" urlprofilexml="" commandline="" additionalpath="" additionalclasspath="" postprocessortype="none" postprocesscommandline="" postprocessadditionalpath="" postprocessgeneratedext=""/></scenarios><MapperMetaTag><MapperInfo srcSchemaPathIsRelative="yes" srcSchemaInterpretAsXML="no" destSchemaPath="" destSchemaRoot="" destSchemaPathIsRelative="yes" destSchemaInterpretAsXML="no"/><MapperBlockPosition></MapperBlockPosition></MapperMetaTag>
</metaInformation>
-->