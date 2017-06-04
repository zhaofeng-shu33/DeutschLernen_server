<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="Entry">
<div id="Noun">
    <h1>
      <span id="stich_wort"><xsl:value-of select="Stichwort"/></span>&#160;
	</h1>	
	<p>
      <xsl:if test="count(Stichwort/@link)">
        <a>
          <xsl:attribute name="href">
            <xsl:value-of select="@link"/>
          </xsl:attribute>
          <img src="icon16_search.png"/>
        </a>
      </xsl:if>
    <span><xsl:value-of select="Genus"/>&#160;<xsl:value-of select="Stichwort"/></span>
	<span>
    <xsl:if test="count(Stichwort/@Audio)">
      
      <img src="snd_sfx.png" style="margin-bottom:-2px" border="0" id="audioImg"></img> <!--add img click listen here-->
	  
    </xsl:if>
	</span> 
	<span>
	 <xsl:value-of select="@category"/>&#160;
	 plural:<xsl:value-of select="Pluralform"/>&#160; 
	 genetiv:<xsl:value-of select="GenitivSingular"/>&#160;
	 </span>
	 </p>
	 <div>
	 <ul>
	 <xsl:for-each select="AllgemeineErläuterungen/Eintrag"><li>
     <span>
	 <xsl:value-of select="Chinesisch"/>
	 </span>
	 	 <ul>
	   <xsl:for-each select="BeispielSammlung/Beispiel"><li><p>
	 <xsl:value-of select="Satz"/></p>
	 <p><xsl:value-of select="Übersetzung"/></p></li>
	 </xsl:for-each>
	 </ul></li>
	 </xsl:for-each>
	 </ul>
    <xsl:if test="count(Kollokationen/K) &gt; 0">
	 <ul style="list-style-type:square;">
	<span>常用搭配</span>
      <xsl:for-each select="Kollokationen/K"><li>
	<xsl:value-of select="."/></li>
	</xsl:for-each>
	</ul>
	</xsl:if>
	
	<xsl:if test="(count(zusammengesetzteWörter/KompositaCollection/K_)+count(zusammengesetzteWörter/KompositaCollection/_K)) &gt; 0">	
	<ul><p>合成词</p>
	<!--<xsl:value-of select="count(zusammengesetzteWörter/KompositaCollection/_K)"/>-->
	<xsl:for-each select="zusammengesetzteWörter/KompositaCollection/K_">
	<li class="horizontal_list"><span>
      <xsl:choose>
        <xsl:when test="count(@link)"><a><xsl:attribute name="href">?wordAddress=N<xsl:value-of select="@link"/></xsl:attribute><xsl:value-of select="."/></a></xsl:when>
        <xsl:otherwise><xsl:value-of select="."/></xsl:otherwise>
      </xsl:choose></span>
	</li>
	</xsl:for-each>
	<xsl:for-each select="zusammengesetzteWörter/KompositaCollection/_K">
	<li class="horizontal_list"><span>
      <xsl:choose>
       <xsl:when test="count(@link)"><a><xsl:attribute name="href">?wordAddress=N<xsl:value-of select="@link"/></xsl:attribute><xsl:value-of select="."/></a></xsl:when>
       <xsl:otherwise><xsl:value-of select="."/></xsl:otherwise>
      </xsl:choose></span>
	</li>
	</xsl:for-each>	
	</ul>
	</xsl:if>

	<xsl:if test="count(zusammengesetzteWörter/abgeleiteteWörter/hierzu) &gt; 0">
	<ul><p style="clear:left">派生词</p>
	<xsl:for-each select="zusammengesetzteWörter/abgeleiteteWörter/hierzu">
	<li class="horizontal_list">
	<span>[<xsl:value-of select="@category"/>]
      <xsl:choose>
        <xsl:when test="count(@link)"><a><xsl:attribute name="href">?wordAddress=N<xsl:value-of select="@link"/></xsl:attribute><xsl:value-of select="."/></a></xsl:when>
        <xsl:otherwise><xsl:value-of select="."/></xsl:otherwise>
      </xsl:choose>
	  </span>
	</li>
	</xsl:for-each></ul>
	</xsl:if>

	<xsl:if test="count(Synonymegruppe/Sym) &gt; 0">
    <ul><p style="clear:left">同义词</p>
    <xsl:for-each select="Synonymegruppe/Sym">
	<li class="horizontal_list">
	<span>
      <xsl:choose>
        <xsl:when test="count(@link)"><a><xsl:attribute name="href">?wordAddress=N<xsl:value-of select="@link"/></xsl:attribute><xsl:value-of select="."/></a></xsl:when>
        <xsl:otherwise><xsl:value-of select="."/></xsl:otherwise>
      </xsl:choose>
	  </span>
	</li>
	</xsl:for-each>
	</ul>
	</xsl:if>
	<xsl:if test="count(Antonymegruppe/Anm) &gt; 0">
    <ul><p style="clear:left">反义词</p>
    <xsl:for-each select="Antonymegruppe/Anm">
	<li class="horizontal_list">
	<span>
      <xsl:choose>
        <xsl:when test="count(@link)"><a><xsl:attribute name="href">?wordAddress=N<xsl:value-of select="@link"/></xsl:attribute><xsl:value-of select="."/></a></xsl:when>
        <xsl:otherwise><xsl:value-of select="."/></xsl:otherwise>
      </xsl:choose>
	  </span>
	</li>
	</xsl:for-each>
	</ul>
	</xsl:if>

	</div>
</div>
	</xsl:template>
</xsl:stylesheet>